# Lab 10: Shopping Cart with Context API and useReducer

## Course: CIS-3340 Full Stack Web Development

## Texas Wesleyan University | Professor Nash

## Estimated Time: 90–120 minutes

---

## Objectives

By completing this lab you will:

- Eliminate prop drilling using the Context API
- Manage complex state with `useReducer`
- Combine Context and `useReducer` into a reusable global store
- Consume context from deeply nested components without prop passing
- Install and configure React Query for server-state management

---

## Prerequisites

- Lab 09 complete (Vite project scaffolding familiar)
- Module 10 video and reading guide complete
- Node 18+ installed

---

## Part 1: Project Setup (10 minutes)

### Step 1 — Scaffold the project

```bash
npm create vite@latest lab10-cart -- --template react
cd lab10-cart
npm install
npm install @tanstack/react-query @tanstack/react-query-devtools
npm run dev
```

### Step 2 — Clean starter files

Replace `src/App.jsx`:

```jsx
function App() {
  return <div><h1>TxWes Bookstore</h1></div>;
}

export default App;
```

Replace `src/index.css`:

```css
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: Arial, sans-serif; background: #f0f2f5; color: #222; }
.container { max-width: 1100px; margin: 0 auto; padding: 24px; }
.grid { display: grid; grid-template-columns: 1fr 340px; gap: 24px; }
.card { background: #fff; border: 1px solid #dde1e7; border-radius: 8px; padding: 16px; margin-bottom: 12px; }
.btn { padding: 8px 16px; border: none; border-radius: 4px; cursor: pointer; font-size: 0.9rem; }
.btn-primary { background: #7B2D8B; color: #fff; }
.btn-danger { background: #dc3545; color: #fff; }
.btn-sm { padding: 4px 10px; font-size: 0.8rem; }
.cart-badge { background: #7B2D8B; color: #fff; border-radius: 50%; padding: 2px 7px; font-size: 0.75rem; margin-left: 6px; }
```

---

## Part 2: Cart Context with useReducer (30 minutes)

### Step 3 — Create the cart reducer

Create `src/context/CartContext.jsx`:

```jsx
import { createContext, useContext, useReducer, useMemo } from 'react';

const CartContext = createContext(null);

function cartReducer(state, action) {
  switch (action.type) {
    case 'ADD': {
      const existing = state.items.find(i => i.id === action.payload.id);
      if (existing) {
        return {
          ...state,
          items: state.items.map(i =>
            i.id === action.payload.id ? { ...i, qty: i.qty + 1 } : i
          ),
        };
      }
      return {
        ...state,
        items: [...state.items, { ...action.payload, qty: 1 }],
      };
    }

    case 'REMOVE':
      return {
        ...state,
        items: state.items.filter(i => i.id !== action.payload),
      };

    case 'UPDATE_QTY':
      return {
        ...state,
        items: state.items.map(i =>
          i.id === action.payload.id
            ? { ...i, qty: Math.max(1, action.payload.qty) }
            : i
        ),
      };

    case 'CLEAR':
      return { items: [] };

    default:
      throw new Error(`Unknown cart action: ${action.type}`);
  }
}

export function CartProvider({ children }) {
  const [state, dispatch] = useReducer(cartReducer, { items: [] });

  const total = state.items.reduce((sum, i) => sum + i.price * i.qty, 0);
  const itemCount = state.items.reduce((sum, i) => sum + i.qty, 0);

  const value = useMemo(
    () => ({ items: state.items, total, itemCount, dispatch }),
    [state.items, total, itemCount]
  );

  return <CartContext.Provider value={value}>{children}</CartContext.Provider>;
}

export function useCart() {
  const ctx = useContext(CartContext);
  if (!ctx) throw new Error('useCart must be used within a CartProvider');
  return ctx;
}
```

### Step 4 — Wire up providers in main.jsx

Update `src/main.jsx`:

```jsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { ReactQueryDevtools } from '@tanstack/react-query-devtools';
import { CartProvider } from './context/CartContext';
import App from './App.jsx';
import './index.css';

const queryClient = new QueryClient({
  defaultOptions: { queries: { staleTime: 2 * 60 * 1000, retry: 1 } },
});

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <QueryClientProvider client={queryClient}>
      <CartProvider>
        <App />
      </CartProvider>
      <ReactQueryDevtools initialIsOpen={false} />
    </QueryClientProvider>
  </React.StrictMode>
);
```

---

## Part 3: Product Catalog with React Query (25 minutes)

### Step 5 — Create mock product data

Create `src/api/products.js`:

```js
const PRODUCTS = [
  { id: 1, title: 'Clean Code', author: 'Robert C. Martin', price: 34.99, genre: 'Engineering' },
  { id: 2, title: 'The Pragmatic Programmer', author: 'Hunt & Thomas', price: 44.99, genre: 'Engineering' },
  { id: 3, title: 'You Don\'t Know JS', author: 'Kyle Simpson', price: 29.99, genre: 'JavaScript' },
  { id: 4, title: 'Designing Data-Intensive Apps', author: 'Martin Kleppmann', price: 54.99, genre: 'Systems' },
  { id: 5, title: 'The Algorithm Design Manual', author: 'Steven Skiena', price: 49.99, genre: 'Algorithms' },
  { id: 6, title: 'Node.js Design Patterns', author: 'Casciaro & Mammino', price: 39.99, genre: 'Node.js' },
];

export function fetchProducts() {
  return new Promise((resolve) => setTimeout(() => resolve(PRODUCTS), 600));
}
```

### Step 6 — Build the ProductCard component

Create `src/components/ProductCard.jsx`:

```jsx
import { useCart } from '../context/CartContext';

function ProductCard({ product }) {
  const { dispatch, items } = useCart();
  const inCart = items.some(i => i.id === product.id);

  return (
    <div className="card">
      <h3>{product.title}</h3>
      <p style={{ color: '#666', fontSize: '0.9rem' }}>{product.author}</p>
      <p style={{ fontWeight: 'bold', margin: '8px 0' }}>${product.price.toFixed(2)}</p>
      <button
        className={`btn btn-primary btn-sm`}
        onClick={() => dispatch({ type: 'ADD', payload: product })}
      >
        {inCart ? 'Add One More' : 'Add to Cart'}
      </button>
    </div>
  );
}

export default ProductCard;
```

### Step 7 — Build the ProductCatalog with useQuery

Create `src/components/ProductCatalog.jsx`:

```jsx
import { useQuery } from '@tanstack/react-query';
import { fetchProducts } from '../api/products';
import ProductCard from './ProductCard';

function ProductCatalog() {
  const { data: products, isLoading, isError, error } = useQuery({
    queryKey: ['products'],
    queryFn: fetchProducts,
  });

  if (isLoading) return <p>Loading products...</p>;
  if (isError) return <p style={{ color: 'red' }}>Error: {error.message}</p>;

  return (
    <div>
      <h2>Catalog ({products.length} books)</h2>
      {products.map(p => <ProductCard key={p.id} product={p} />)}
    </div>
  );
}

export default ProductCatalog;
```

---

## Part 4: Shopping Cart Display (20 minutes)

### Step 8 — Build CartItem component

Create `src/components/CartItem.jsx`:

```jsx
import { useCart } from '../context/CartContext';

function CartItem({ item }) {
  const { dispatch } = useCart();

  return (
    <div className="card" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
      <div style={{ flexGrow: 1 }}>
        <strong>{item.title}</strong>
        <p style={{ fontSize: '0.85rem' }}>${item.price.toFixed(2)} each</p>
      </div>
      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
        <input
          type="number"
          min="1"
          value={item.qty}
          style={{ width: '48px', padding: '4px', borderRadius: '4px', border: '1px solid #ccc' }}
          onChange={e =>
            dispatch({ type: 'UPDATE_QTY', payload: { id: item.id, qty: parseInt(e.target.value) || 1 } })
          }
        />
        <button
          className="btn btn-danger btn-sm"
          onClick={() => dispatch({ type: 'REMOVE', payload: item.id })}
        >
          ×
        </button>
      </div>
    </div>
  );
}

export default CartItem;
```

### Step 9 — Build CartPanel component

Create `src/components/CartPanel.jsx`:

```jsx
import { useCart } from '../context/CartContext';
import CartItem from './CartItem';

function CartPanel() {
  const { items, total, itemCount, dispatch } = useCart();

  return (
    <div>
      <h2>Cart <span className="cart-badge">{itemCount}</span></h2>

      {items.length === 0 ? (
        <p style={{ color: '#888', padding: '16px 0' }}>Your cart is empty.</p>
      ) : (
        <>
          {items.map(item => <CartItem key={item.id} item={item} />)}
          <div style={{ borderTop: '2px solid #dde1e7', paddingTop: '12px', marginTop: '8px' }}>
            <p style={{ fontSize: '1.1rem', fontWeight: 'bold' }}>
              Total: ${total.toFixed(2)}
            </p>
            <div style={{ display: 'flex', gap: '8px', marginTop: '12px' }}>
              <button className="btn btn-primary" style={{ flexGrow: 1 }}>
                Checkout
              </button>
              <button
                className="btn btn-danger"
                onClick={() => dispatch({ type: 'CLEAR' })}
              >
                Clear
              </button>
            </div>
          </div>
        </>
      )}
    </div>
  );
}

export default CartPanel;
```

### Step 10 — Assemble App.jsx

Update `src/App.jsx`:

```jsx
import ProductCatalog from './components/ProductCatalog';
import CartPanel from './components/CartPanel';

function App() {
  return (
    <div className="container">
      <header style={{ marginBottom: '24px' }}>
        <h1>TxWes Bookstore</h1>
        <p style={{ color: '#666' }}>Powered by Context API + useReducer + React Query</p>
      </header>
      <div className="grid">
        <ProductCatalog />
        <CartPanel />
      </div>
    </div>
  );
}

export default App;
```

---

## Expected Output

When the application loads correctly:

- A 600ms loading spinner appears, then the catalog renders 6 books.
- Clicking "Add to Cart" adds the book to the cart panel and updates the item count badge.
- Adding the same book again increments the quantity.
- The quantity input allows changing the amount; the total updates immediately.
- The × button removes an item from the cart.
- The Clear button empties the cart.
- The React Query Devtools icon appears at the bottom-right corner.
- No props are passed through intermediate components — `ProductCard` and `CartItem` both call `useCart()` directly.

---

## Deliverables

Submit your `lab10-cart` folder zipped (excluding `node_modules`). Required files:

1. `src/context/CartContext.jsx` — provider, reducer, custom hook
2. `src/components/ProductCard.jsx`
3. `src/components/ProductCatalog.jsx` — uses `useQuery`
4. `src/components/CartItem.jsx`
5. `src/components/CartPanel.jsx`
6. `src/api/products.js`
7. `src/main.jsx` — providers configured

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Cart context provides items, total, itemCount, dispatch | 15 |
| useReducer handles ADD, REMOVE, UPDATE_QTY, CLEAR correctly | 20 |
| useQuery fetches products with loading and error states | 20 |
| ProductCard and CartItem consume context without prop drilling | 15 |
| Cart total and item count update correctly after all actions | 15 |
| No console errors; providers correctly nested in main.jsx | 10 |
| Code quality: no direct mutation, consistent naming | 5 |
| **Total** | **100** |
