import { useContext } from "react";
import CartContext from "./Context";

function DeleteProduct({ productName, onDeleteProduct }) {
    const cart = useContext(CartContext);
    const handleDeleteClick = () => {
        onDeleteProduct(productName);
    };
    // const deleteItem = (itemToRemove) => {
    //     const updatedCart = cart.filter((item) => item.product !== itemToRemove);
    //     console.log("Producto eliminado:", itemToRemove);
    //     console.log("Nuevo carrito:", updatedCart);
    // }
    return (
        <>
            <button onClick={handleDeleteClick}>X</button>
        </>
    );
}


export default DeleteProduct;