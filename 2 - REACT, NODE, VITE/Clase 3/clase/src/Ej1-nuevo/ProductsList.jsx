import { useContext } from "react";
import CartContext from "./Context";
import DeleteProduct from "./DeleteProduct";

/*
En este componente se juntan los productos y los botones para eliminarlos o modificar sus cantidades

|MOUSE GAMER        | Cantidad  | Eliminar |
|$2500              |  |  3  |  |    X     | 
|                   |  |+| |-|  |          | 

*/
function ProductsList() {
    const cart = useContext(CartContext);

    const handleDeleteProduct = (productName) => {
        const updatedCart = cart.filter((item) => item.product !== productName);
        console.log("Producto eliminado:", productName);
        console.log("Nuevo carrito:", updatedCart);
    };
    const handleProductQuantity = (productQuantity) => {
        const updatedCart = (item) => {
            item

        };
    };
    return (
        <>
            <ul>
                {cart.map((item, index) => (
                    <div className="product-display">
                        <li key={index}>
                            {item.product}
                        </li>
                        <li>
                            ${item.price}
                        </li>
                        <li>
                            {item.quantity}
                        </li>
                        <DeleteProduct
                            productName={item.product}
                            onDeleteProduct={handleDeleteProduct}
                        />
                    </div>
                ))}
            </ul>
        </>
    );
}

export default ProductsList;