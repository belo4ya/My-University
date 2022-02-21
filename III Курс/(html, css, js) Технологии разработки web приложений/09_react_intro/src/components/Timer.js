import React, {useEffect, useState} from 'react';

const Timer = () => {
  const [seconds, setSeconds] = useState(0)
  const [isActive, setIsActive] = useState(false)

  const toggle = () => {
    setIsActive(!isActive)
  }

  useEffect(() => {
    let interval = null
    if (isActive) {
      interval = setInterval(() => {
        setSeconds(seconds => seconds + 1)
      }, 1000)
    } else if (!isActive && seconds !== 0) {
      clearInterval(interval)
    }
    return () => clearInterval(interval)
  }, [isActive, seconds])

  return (
    <div className="timer-card" onClick={toggle}>
      <div className={'timer' + (isActive ? '' : ' is-disabled')}>{seconds}</div>
    </div>
  )
}

export default Timer