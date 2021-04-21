import React from "react";
import { hot } from "react-hot-loader";

import "./index.css";

const BoardSizeSelector = (props) => {
  const { handleChangeSize, boardSize } = props;

  return (
    <div className="board-size-select-container">
      <h5>Choose Board Size</h5>
      <select
        type="number"
        name="boardSize"
        onChange={handleChangeSize}
        value={boardSize}
      >
        {Array(75)
          .fill(0)
          .map((_, i) => (
            <option id={`${i}-option`} value={i + 1}>
              {i + 1}
            </option>
          ))}
      </select>
    </div>
  );
};

export default hot(module)(BoardSizeSelector);
