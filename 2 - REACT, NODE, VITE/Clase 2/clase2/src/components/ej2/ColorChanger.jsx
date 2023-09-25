import React from 'react';

function ColorChanger(props) {
  const { color } = props;
  const changeColor = () => {
    document.body.style.backgroundColor = color;
  };
  return (
    <>
      <a href="#" onClick={() => changeColor(props.color)}>{props.name}</a>
    </>
  );
}

export default ColorChanger;
