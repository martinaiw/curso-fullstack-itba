
// import Google from './components/Google';
// import Primero from './components/Primero';
// import Segundo from './components/Segundo';

import Button from "./components/Clase/Button";
import Hooks from "./components/Clase/Hooks";
import ProductCategoryRow from "./components/Clase/ProductCategoryRow";
import ProductRow from "./components/Clase/ProductRow";
import ProductTable from "./components/Clase/ProductTable";
//nuevos componentes ejemplos pdf clase 1
import { Profile } from "./components/Gallery"
import Gallery from "./components/Gallery";
import { Encabecaco } from "./components/Encabecaco";
import { Butono } from "./components/Butono";
import { List } from "./components/List";
import { Counter } from "./components/Counter";
import { TitleUpdater } from "./components/TitleUpdater";


function App() {
    const items = [
        { id: 1, text: "Item 1" },
        { id: 2, text: "Item 2" },
        { id: 3, text: "Item 3" }
    ];
    return (
        <>
            {/* <Button primary={"HOLA AMIGOS"} text={"Mini botón"}/>
            <Button primary={""} text={"Gran botón"}/> 
            <ProductCategoryRow/>
            <ProductRow/>
            <ProductTable/>*/}
            <Gallery />
            <Profile />
            <br />
            <br />
            <Encabecaco title="Mi sitio web" />
            <Butono
                text="Haz clic aquí"
                onClick={() => alert("Botón presionado")}
            />
            <List items={items} />
            <Counter/>
            <TitleUpdater/>

        </>

    );
}
export default App;