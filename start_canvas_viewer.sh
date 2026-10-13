#!/usr/bin/env bash
# ==============================================================================
# Texas Wesleyan University - Local Canvas LMS Course Simulator Manager
# ==============================================================================
# Starts, stops, or checks status of the local Canvas viewer on your laptop.
# Usage:
#   ./start_canvas_viewer.sh          # Start viewer in background (default port 3000)
#   ./start_canvas_viewer.sh 8080     # Start viewer on port 8080
#   ./start_canvas_viewer.sh fg       # Start in foreground (interactive)
#   ./start_canvas_viewer.sh stop     # Stop running viewer
#   ./start_canvas_viewer.sh restart  # Restart viewer
#   ./start_canvas_viewer.sh status   # Check status
#   ./start_canvas_viewer.sh logs     # Tail output logs
# ==============================================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VIEWER_PY="$SCRIPT_DIR/tools/utilities/local_canvas_viewer.py"
PID_FILE="$SCRIPT_DIR/.canvas_viewer.pid"
LOG_FILE="$SCRIPT_DIR/.canvas_viewer.log"
DEFAULT_PORT=3000

get_running_pid() {
    pgrep -f "local_canvas_viewer.py" | head -n 1
}

start_server() {
    local PORT="${1:-$DEFAULT_PORT}"
    local EXISTING_PID=$(get_running_pid)

    if [ -n "$EXISTING_PID" ]; then
        echo "⚠️  Canvas LMS Simulator is ALREADY RUNNING (PID: $EXISTING_PID)."
        echo "🌐 Access your courses at: http://localhost:$PORT"
        echo "$EXISTING_PID" > "$PID_FILE"
        exit 0
    fi

    echo "🚀 Starting Texas Wesleyan Canvas LMS Course Simulator on port $PORT..."
    python3 "$VIEWER_PY" "$PORT" > "$LOG_FILE" 2>&1 &
    local NEW_PID=$!
    echo $NEW_PID > "$PID_FILE"
    disown $NEW_PID 2>/dev/null
    sleep 1

    if ps -p "$NEW_PID" > /dev/null 2>&1; then
        echo "================================================================="
        echo "🏛️  Texas Wesleyan University - Canvas LMS Simulator ACTIVE"
        echo "================================================================="
        echo "📍 URL:     http://localhost:$PORT"
        echo "📄 PID:     $NEW_PID"
        echo "📋 Log:     $LOG_FILE"
        echo "💡 To stop: ./start_canvas_viewer.sh stop"
        echo "================================================================="
        
        # Open in default browser if in GUI desktop session
        if which xdg-open > /dev/null 2>&1 && [ -n "$DISPLAY" ]; then
            xdg-open "http://localhost:$PORT" > /dev/null 2>&1 &
        fi
    else
        echo "❌ Failed to start Canvas Simulator. Check logs at: $LOG_FILE"
        cat "$LOG_FILE"
        exit 1
    fi
}

start_foreground() {
    local PORT="${1:-$DEFAULT_PORT}"
    echo "🏛️  Launching Texas Wesleyan Canvas LMS Simulator in FOREGROUND on port $PORT..."
    echo "💡 Press Ctrl+C to terminate."
    python3 "$VIEWER_PY" "$PORT"
}

stop_server() {
    local RUNNING_PIDS=$(pgrep -f "local_canvas_viewer.py")
    if [ -n "$RUNNING_PIDS" ]; then
        echo "🛑 Stopping Canvas Simulator (PID(s): $RUNNING_PIDS)..."
        kill $RUNNING_PIDS 2>/dev/null
        sleep 1
        kill -9 $RUNNING_PIDS 2>/dev/null
        rm -f "$PID_FILE"
        echo "✓ Canvas Simulator stopped successfully."
    else
        rm -f "$PID_FILE"
        echo "ℹ️  Canvas Simulator is not currently running."
    fi
}

status_server() {
    local EXISTING_PID=$(get_running_pid)
    if [ -n "$EXISTING_PID" ]; then
        echo "✅ Canvas LMS Simulator is RUNNING (PID: $EXISTING_PID)"
        echo "🌐 Open in browser: http://localhost:$DEFAULT_PORT"
        echo "📄 Recent logs:"
        tail -n 8 "$LOG_FILE" 2>/dev/null || echo "   (No logs yet)"
    else
        echo "⚪ Canvas LMS Simulator is STOPPED."
        echo "💡 Run './start_canvas_viewer.sh' to launch."
    fi
}

case "$1" in
    stop)
        stop_server
        ;;
    restart)
        stop_server
        sleep 1
        start_server "$2"
        ;;
    status)
        status_server
        ;;
    fg|foreground)
        stop_server
        sleep 1
        start_foreground "$2"
        ;;
    log|logs)
        tail -f "$LOG_FILE"
        ;;
    ""|*[0-9]*)
        start_server "$1"
        ;;
    *)
        echo "Usage: $0 [start|stop|restart|status|logs|fg|<port>]"
        exit 1
        ;;
esac
