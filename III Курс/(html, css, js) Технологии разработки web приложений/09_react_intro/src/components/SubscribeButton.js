import React, {useState} from 'react';

const SubscribeButton = () => {
  const [state, setState] = useState();

  const onClick = (e) => {
    e.preventDefault();

  }
  return (
    <div>
      <button onClick={onClick}>{}</button>
    </div>
  );
};

export default SubscribeButton;