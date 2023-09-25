import { useContext, useState } from "react";
import CartContext from "./Context";
/*
En este componente se manejará la cantidad de productos del mismo tipo
CANTIDAD |+| |-|
*/
function AddProduct() {
    const cart = useContext(CartContext);
    const [itemToAdd, setItemToAdd] = useState({ product: "", price: 0, quantity: 1 })

    const addItem = () => {
        const updatedCart = [...cart, itemToAdd];
        console.log("Producto añadido")
        setItemToAdd({ product: "", price: 0, quantity: 1 }); // Reinicia el formulario
    };
    return (
        <>
            <form>
                <input
                    type="text"
                    placeholder="Producto"
                    value={itemToAdd.product}
                    onChange={(e) => setItemToAdd({ ...itemToAdd, product: e.target.value })}
                />
                $<input
                    type="number"
                    placeholder="Precio"
                    value={itemToAdd.price}
                    onChange={(e) => setItemToAdd({ ...itemToAdd, price: e.target.value })}
                />
                <input
                    type="number"
                    placeholder="Cantidad"
                    value={itemToAdd.quantity}
                    onChange={(e) => setItemToAdd({ ...itemToAdd, quantity: e.target.value })}

                />
                <button onClick={() => addItem({})}>Agregar</button>
            </form>
        </>
    );
}

export default AddProduct;