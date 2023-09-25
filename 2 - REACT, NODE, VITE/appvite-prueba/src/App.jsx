import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom'
import Inicio from './components/inicio'
import Transferencias from './components/Transferencias'
import Cotizaciones from './components/Cotizaciones'
import GetPokemon from './components/GetPokemon';

function NoMatch() {
  return (
    <div>
      <h1>404: La página que estás buscando no existe!</h1>
      <p>Por favor verificá y volvé a intentarlo</p>
    </div>
  );
}
/*Puede colocarlo dentro de App porque está relacionado con todo lo que 
hay acá adentro, aunque tambien podria ponerlo en un archivo aparte como
hice con Transferencias o Cotizaciones*/




function App() {

  return (
    <Router>
      <nav style={{ margin: 20 }}>
        <Link to='/' style={{padding: 10}}>Inicio</Link>
        <Link to='/transferencias' style={{padding: 10}}>Transferencias</Link>
        <Link to='/coti' style={{padding: 10}}>Cotizaciones</Link>
        <Link to='/poke' style={{padding: 10}}>Pokemones</Link>
        {/* Con Link to no recarga la página, si no que reemplaza componentes
        podemos verlo en el navegador cuando navegamos entre los diferentes links
        que el logo en la pestaña arriba no se mueve, esto significa que no se recarga.
        A esto lo llamamos Single Page Application*/}
      </nav>
      <Routes>
        <Route path='/' element={<Inicio />} />
        <Route path='/transferencias' element={<Transferencias />} />
        <Route path='/coti' element={<Cotizaciones />} />
        <Route path='/poke' element={<GetPokemon />} />
        {/* El nombre del path no debe necesariamente coincidir con el nombre
        del componente */}
        <Route path='*' element={<NoMatch />} />
      </Routes>
    </Router>
  )
}

export default App
