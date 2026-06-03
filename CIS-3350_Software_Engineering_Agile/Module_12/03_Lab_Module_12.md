# Lab Activity: Module 12 — Software Design Patterns

## Course: CIS-3350 Software Engineering and Agile

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Scrum.org PSM I / Software Engineering Best Practices

---

## Lab Overview

**Title:** Implementing Design Patterns in a Notification System

**Estimated Time:** 90–120 minutes

**Language Options:** JavaScript or Python — choose one

**Submission:** Upload your source files and a screenshot of the program running

---

## Learning Objectives

By completing this lab you will:

- Implement at least three design patterns from different categories in a coherent system
- Apply the Factory pattern to create notification channel objects at runtime
- Use the Observer pattern to decouple event subjects from notification handlers
- Apply the Command pattern to support undoable notification scheduling
- Identify which pattern solves which design constraint in a realistic scenario

---

## Background

You are building a notification scheduling system for a university event management application. The system must:

1. Support multiple notification channels: Email, SMS, and Push notification
2. Allow event managers to subscribe multiple channels to a single event
3. Notify all subscribed channels automatically when an event status changes
4. Support scheduling and canceling (undoing) notifications

This scenario deliberately requires three patterns — one from each category:

- **Factory Method** (Creational): create notification channels without hard-coding channel types in the event code
- **Observer** (Behavioral): notify all subscribed channels when an event changes status
- **Command** (Behavioral): support scheduling and undoing of notification sends

---

## Starter Code

Read this interface sketch before writing any code. You will implement each class using TDD from Module 10 — write tests before implementation.

### JavaScript Interface Sketch

```javascript
// notification_channels.js — you will implement these
class NotificationChannel {
  send(eventName, message) {
    throw new Error('send() must be implemented');
  }
}

class EmailChannel extends NotificationChannel { /* ... */ }
class SmsChannel extends NotificationChannel { /* ... */ }
class PushChannel extends NotificationChannel { /* ... */ }

// notification_factory.js
function createChannel(type) { /* Factory Method */ }

// event_subject.js — Observer subject
class EventSubject {
  subscribe(channel) { /* ... */ }
  unsubscribe(channel) { /* ... */ }
  changeStatus(newStatus) { /* notifies all channels */ }
}

// notification_command.js — Command pattern
class SendNotificationCommand {
  execute() { /* send the notification */ }
  undo() { /* cancel / log the cancellation */ }
}

class NotificationScheduler {
  schedule(command) { /* add to queue, execute immediately for this lab */ }
  cancel() { /* undo the last scheduled command */ }
}
```

### Python Interface Sketch

```python
# notification_channels.py
class NotificationChannel:
    def send(self, event_name: str, message: str):
        raise NotImplementedError

class EmailChannel(NotificationChannel): pass
class SmsChannel(NotificationChannel): pass
class PushChannel(NotificationChannel): pass

# notification_factory.py
def create_channel(channel_type: str) -> NotificationChannel:
    pass  # Factory Method

# event_subject.py
class EventSubject:
    def subscribe(self, channel): pass
    def unsubscribe(self, channel): pass
    def change_status(self, new_status): pass

# notification_command.py
class SendNotificationCommand:
    def execute(self): pass
    def undo(self): pass

class NotificationScheduler:
    def schedule(self, command): pass
    def cancel(self): pass
```

---

## Lab Tasks

### Task 1 — Implement Notification Channels (15 min)

Implement `EmailChannel`, `SmsChannel`, and `PushChannel`. Each channel's `send()` method should print a formatted message indicating the channel type.

Write one test per channel before implementing:

```javascript
// JavaScript test example
test('EmailChannel.send prints email notification', () => {
  const consoleSpy = jest.spyOn(console, 'log');
  const channel = new EmailChannel();
  channel.send('Graduation Ceremony', 'Event starts at 10am');
  expect(consoleSpy).toHaveBeenCalledWith(
    expect.stringContaining('[EMAIL]')
  );
  consoleSpy.mockRestore();
});
```

```python
# Python test example
from unittest.mock import patch
from notification_channels import EmailChannel

def test_email_channel_send_includes_email_label():
    channel = EmailChannel()
    with patch('builtins.print') as mock_print:
        channel.send('Graduation Ceremony', 'Event starts at 10am')
        output = mock_print.call_args[0][0]
        assert '[EMAIL]' in output
```

### Task 2 — Implement the Factory Method (15 min)

Implement `createChannel(type)` that returns the correct channel object based on the type string. Handle invalid types by raising an error.

Write tests for:

- `createChannel('email')` returns an `EmailChannel` instance
- `createChannel('sms')` returns an `SmsChannel` instance
- `createChannel('push')` returns a `PushChannel` instance
- `createChannel('fax')` raises an error (unknown type)

```javascript
// JavaScript
test('factory creates EmailChannel for "email" type', () => {
  const channel = createChannel('email');
  expect(channel).toBeInstanceOf(EmailChannel);
});

test('factory throws for unknown channel type', () => {
  expect(() => createChannel('fax')).toThrow();
});
```

### Task 3 — Implement the Observer Pattern (20 min)

Implement `EventSubject` with `subscribe()`, `unsubscribe()`, and `changeStatus()`. When `changeStatus()` is called, all subscribed channels should have their `send()` method called with the event name and a message describing the new status.

Write tests for:

- Subscribing one channel: calling `changeStatus()` invokes that channel's `send()` exactly once
- Subscribing two channels: both are notified
- Unsubscribing a channel: it is no longer notified after unsubscription
- Subscribing zero channels: `changeStatus()` runs without error

```javascript
// JavaScript test example — using mocks
test('changeStatus notifies all subscribed channels', () => {
  const channel1 = { send: jest.fn() };
  const channel2 = { send: jest.fn() };
  const event = new EventSubject('Spring Convocation');

  event.subscribe(channel1);
  event.subscribe(channel2);
  event.changeStatus('Cancelled');

  expect(channel1.send).toHaveBeenCalledWith(
    'Spring Convocation',
    expect.stringContaining('Cancelled')
  );
  expect(channel2.send).toHaveBeenCalledTimes(1);
});
```

### Task 4 — Implement the Command Pattern (20 min)

Implement `SendNotificationCommand` with `execute()` and `undo()`. The command holds a reference to a channel, an event name, and a message. `execute()` calls `channel.send()`. `undo()` prints a cancellation message (simulating a scheduled notification being cancelled before delivery).

Implement `NotificationScheduler` with `schedule(command)` (executes immediately for this lab) and `cancel()` (undoes the last command).

Write tests for:

- `schedule(command)` calls `command.execute()`
- `cancel()` calls `undo()` on the most recently scheduled command
- `cancel()` when no commands have been scheduled handles gracefully (no error)

```python
# Python test example
from unittest.mock import MagicMock
from notification_command import SendNotificationCommand, NotificationScheduler

def test_scheduler_executes_command_when_scheduled():
    mock_channel = MagicMock()
    cmd = SendNotificationCommand(mock_channel, 'Finals Week', 'Library extended hours')
    scheduler = NotificationScheduler()
    scheduler.schedule(cmd)
    mock_channel.send.assert_called_once_with('Finals Week', 'Library extended hours')

def test_cancel_undoes_last_command():
    mock_channel = MagicMock()
    cmd = SendNotificationCommand(mock_channel, 'Finals Week', 'Library extended hours')
    scheduler = NotificationScheduler()
    scheduler.schedule(cmd)
    scheduler.cancel()
    # After cancel, verify undo was called (mock the undo method)
```

### Task 5 — Integration: Wire Everything Together (15 min)

Write a short integration script that demonstrates all three patterns working together:

```javascript
// integration_demo.js
const { createChannel } = require('./notification_factory');
const EventSubject = require('./event_subject');
const { SendNotificationCommand, NotificationScheduler } = require('./notification_command');

// Factory creates channels
const emailChannel = createChannel('email');
const smsChannel = createChannel('sms');

// Observer subscribes channels to event
const graduationEvent = new EventSubject('Spring Graduation');
graduationEvent.subscribe(emailChannel);
graduationEvent.subscribe(smsChannel);

// Command schedules and cancels a notification
const scheduler = new NotificationScheduler();
const pushChannel = createChannel('push');
const urgentNotice = new SendNotificationCommand(
  pushChannel,
  'Spring Graduation',
  'Venue change: moving to gymnasium'
);

scheduler.schedule(urgentNotice);  // sends immediately
// Decision made: cancel the last notification
scheduler.cancel();                 // logs cancellation

// Observer fires
graduationEvent.changeStatus('Confirmed');
```

Run the script and verify the output shows:

1. The command notification sent and then cancelled
2. Both the email and SMS channels notified of the status change

---

## Deliverables

Submit a ZIP file containing:

1. All source files (channels, factory, event subject, command, scheduler)
2. All test files
3. The integration demo script
4. A screenshot of the integration demo running in a terminal
5. A `pattern_notes.txt` file with one paragraph per pattern describing: which design constraint it solved and what would be harder without it

---

## Grading Rubric

| Criterion | Points | Description |
|-----------|--------|-------------|
| Factory implementation + tests | 20 | All channel types created correctly; unknown type handled; tests pass |
| Observer implementation + tests | 25 | Subscribe, unsubscribe, and notify all work; all four test cases pass |
| Command implementation + tests | 25 | Execute and undo work; scheduler schedule/cancel work; edge case handled |
| Integration demo runs correctly | 15 | Output shows all three patterns contributing to the result |
| Pattern notes | 15 | Three clear paragraphs connecting each pattern to its design constraint |
| **Total** | **100** | |

---

## Common Mistakes to Avoid

- Calling `send()` directly in `EventSubject` instead of delegating to the channel's `send()` method — this defeats Observer's loose coupling
- Storing the channel type string in the Observer subject — the subject should not know channel types exist; it only knows channels have a `send()` method
- Forgetting to test the `unsubscribe()` path — observers that cannot be removed are a memory leak
- In the Command pattern, not storing the command in history before executing it — `cancel()` needs access to the command after `schedule()` runs

---

## Extension Challenge (Optional)

Add a fourth pattern: implement a `NotificationFacade` class that provides a single `notifyEvent(eventName, status, channels)` method that internally handles factory creation, observer subscription, and command scheduling. This is the Facade pattern: one simple call replacing the multi-step process in the integration demo.
