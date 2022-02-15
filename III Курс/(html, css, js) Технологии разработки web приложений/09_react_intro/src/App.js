import './App.css';
import LikeButton from "./components/LikeButton";
import DislikeButton from "./components/DislikeButton";
import SubscribeButton from "./components/SubscribeButton";

function App() {
  return (
    <div>
      <LikeButton/>
      <DislikeButton/>
      <SubscribeButton/>
    </div>
  );
}

export default App;
