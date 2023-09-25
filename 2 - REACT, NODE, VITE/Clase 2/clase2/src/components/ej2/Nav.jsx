import React from 'react';
import ColorChanger from './ColorChanger';
function Nav(props) {
  return (
    <nav>
      <ul>
        <li>
          <ColorChanger name="Rojo" color='red' />
        </li>
        <li>
          <ColorChanger name="Verde" color='green' />
        </li>
        <li>
          <ColorChanger name="Azul" color='blue' />
        </li>
      </ul>
    </nav>
  );
}

export default Nav;
