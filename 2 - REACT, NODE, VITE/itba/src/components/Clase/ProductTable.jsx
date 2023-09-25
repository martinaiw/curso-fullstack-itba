import ProductCategoryRow from "./ProductCategoryRow";


function ProductTable({ products }) {
    const rows = [];
    let lastCategory = null;
    products.forEach((product) => {
        if (product.category !== lastCategory) {
            rows.push(
                <ProductCategoryRow
                    category={product.category}
                    key={product.category} />
            );
        }
    });

}
export default ProductTable;