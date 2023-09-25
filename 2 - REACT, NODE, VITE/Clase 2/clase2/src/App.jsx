import logo from './logo.svg';
import './App.css';
import Header from './components/ej2/Header';
import Footer from './components/ej2/Footer';
import Nav from './components/ej2/Nav';
import Section from './components/ej2/Section';
import React, { useEffect } from 'react';
import ConditionalRendering from './components/ej3/ConditionalRendering';
import TodoList from './components/ej4/TodoList';


function App() {
  useEffect(() => {
    document.title = "Mi Página Interactiva"; // Cambia el título de la página
  }, []);
  return (
    <>
    <TodoList/>
    </>
  );
}

export default App;




{/* Ejercicio 2
<link stylesheet="App.css" />
<Header />
<Nav className="nav-"/>
<Section/>
<Footer className="footer"/> */}

{/* Ejercicio 3 
<ConditionalRendering/> */}