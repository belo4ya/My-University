import React from 'react';
import likeSrc from "../assets/like.png";

export const LikeButton = ({onClick, className, alt, children}) => {
  return (
    <button className={className} onClick={onClick}>
      <img className="like-btn__icon" alt={alt} src={likeSrc}/>
      <div className="like-btn__text">{children}</div>
    </button>
  )
}
