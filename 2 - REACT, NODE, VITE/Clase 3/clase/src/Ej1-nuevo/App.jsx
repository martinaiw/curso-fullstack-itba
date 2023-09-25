
/*En App se juntan los otros componentes

=================================================
++              CARRITO DE COMPRAS             ++
++    ______________________________________   ++
++   |MOUSE GAMER   |  Cantidad | Eliminar |   ++
++   |$2500         |  |  3  |  |          |   ++
++   |              |  |+| |-|  |    X     |   ++ 
++   |______________|___________|__________|   ++
++    ______________________________________   ++
++   |TECLADO GAMER | Cantidad  | Eliminar |   ++
++   |$7500         |  |  1  |  |          |   ++ 
++   |              |  |+| |-|  |    X     |   ++ 
++   |______________|___________|__________|   ++
++    ______________________________________   ++
++   |LAPICERAS     | Cantidad  | Eliminar |   ++
++   |$250          |  |  5  |  |    X     |   ++ 
++   |              |  |+| |-|  |    X     |   ++ 
++   |______________|___________|__________|   ++
=================================================
*/

import React from "react";
import CartContext, { CartProvider } from "./Context";
import ManageProducts from "./AddProduct";
import ProductsList from "./ProductsList";

function App() {
  const cart = [
    { product: "banana", price: 45, quantity: 3 },
    { product: "apple", price: 32, quantity: 4 }
  ];
  return (
    <>
      <CartProvider value={cart}>
        <h1>CARRITO DE COMPRAS</h1>
        <ProductsList/>
        <ManageProducts/>
      </CartProvider>
    </>

  );
}

export default App;
