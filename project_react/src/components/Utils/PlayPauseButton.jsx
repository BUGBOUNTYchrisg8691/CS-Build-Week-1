import React from "react";
import { hot } from "react-hot-loader";

import "./index.css";

const PlayPauseButton = (props) => {
  const { play, setPlay } = props;

  const handleClick = () => {
    setPlay(!play);
  };

  return (
    <button className="play-button" type="submit" onClick={handleClick}>
      {play ? "Pause" : "Play"}
    </button>
  );
};

export default hot(module)(PlayPauseButton);
