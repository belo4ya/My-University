import React from 'react';

const SubscribeButton = ({subscribed, onClick}) => {
  return (
    <button className={'subscribe-btn' + (subscribed ? ' subscribed' : '')} onClick={onClick}>
      {subscribed ? 'Вы подписаны' : 'Подписаться'}
    </button>
  );
};

export default SubscribeButton;