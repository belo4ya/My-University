import {useEffect, useState} from "react";
import SubscribeButton from "./components/SubscribeButton";
import {LikeButton} from "./components/LikeButton";
import Timer from "./components/Timer";

const getSubscribed = () => {
  return false
}

const getNLikes = () => {
  return 32
}

const getNDislikes = () => {
  return 0
}

const STATUS = {NOT_SET: 0, LIKE: 1, NOT_LIKE: 2}

function App() {
  const [likeState, setLikeState] = useState({nLikes: 0, nDislikes: 0, status: STATUS.NOT_SET})
  const [subscribed, setSubscribed] = useState(false)

  const handleLikeBtn = (e) => {
    e.preventDefault()
    let nLikes, nDislikes, status
    if (likeState.status === STATUS.LIKE) {
      [nLikes, nDislikes, status] = [likeState.nLikes - 1, likeState.nDislikes, STATUS.NOT_SET]
    } else if (likeState.status === STATUS.NOT_LIKE) {
      [nLikes, nDislikes, status] = [likeState.nLikes + 1, likeState.nDislikes - 1, STATUS.LIKE]
    } else {
      [nLikes, nDislikes, status] = [likeState.nLikes + 1, likeState.nDislikes, STATUS.LIKE]
    }
    setLikeState({nLikes, nDislikes, status})
  }

  const handleDislikeBtn = (e) => {
    e.preventDefault()
    let nLikes, nDislikes, status
    if (likeState.status === STATUS.NOT_LIKE) {
      [nLikes, nDislikes, status] = [likeState.nLikes, likeState.nDislikes - 1, STATUS.NOT_SET]
    } else if (likeState.status === STATUS.LIKE) {
      [nLikes, nDislikes, status] = [likeState.nLikes - 1, likeState.nDislikes + 1, STATUS.NOT_LIKE]
    } else {
      [nLikes, nDislikes, status] = [likeState.nLikes, likeState.nDislikes + 1, STATUS.NOT_LIKE]
    }
    setLikeState({nLikes, nDislikes, status})
  }

  const handleSubscribeBtn = (e) => {
    e.preventDefault()
    setSubscribed(!subscribed)
  }

  useEffect(() => {
    const subscribed = getSubscribed()
    const [nLikes, nDislikes] = [getNLikes(), getNDislikes()]
    console.log(`Полученные данные: subscribed=${subscribed} nLikes=${nLikes}, nDislikes=${nDislikes}`)
    setSubscribed(subscribed)
    setLikeState({
      nLikes: nLikes,
      nDislikes: nDislikes,
      status: STATUS.NOT_SET
    })
  }, [])

  return (
    <div className="container">
      <div className="centred-container">
        <Timer/>
        <div className="centred-bar">
          <div className="col-container">
            <LikeButton
              className={'like-btn' + (likeState.status === STATUS.LIKE ? ' pressed' : '')}
              onClick={handleLikeBtn}
              alt="like">
              {likeState.nLikes}
            </LikeButton>
            <LikeButton
              className={'like-btn dislike' + (likeState.status === STATUS.NOT_LIKE ? ' pressed' : '')}
              onClick={handleDislikeBtn}
              alt="dislike">
              Не нравится
            </LikeButton>
          </div>
          <div className="col-container">
            <SubscribeButton subscribed={subscribed} onClick={handleSubscribeBtn}/>
          </div>
        </div>
      </div>
    </div>
  )
}

export default App;
