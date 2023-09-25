import logo from './logo.svg';
import './App.css';
import Button from './components/Button.jsx';
import Header from './components/Header.js';
import Footer from './components/Footer.js';
import Cards from './components/Cards';
import Counter from './components/Counter';
import ToDoList from './components/ToDoList';

function App() {
  const items = [ 
    { id: 1, text: "Item 1" }, 
    { id: 2, text: "Item 2" }, 
    { id: 3, text: "Item 3" } 
  ]; 
  return (
    <>
    {/* <Header/>
    <h3>Esto que ves acá abajo es un botón, presiónalo!</h3>
    <Button/>
    <Cards title = "Mi primera aplicacion en React"/>
    <Cards descripcion = "Le estoy pasando dos props al componente Cards, este es el componente description"/>
    <Counter/>
    <Footer/> */}
    <ToDoList/>
    </>
  );
}

export default App;
