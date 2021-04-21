import React from "react";
import { hot } from "react-hot-loader";

import "./Cell.css";

const Cell = (props) => {
  const { value, handleCellClick } = props;

  const [cellVal, setCellVal] = React.useState(value);

  return (
    <button
      className={`${cellVal ? "cell-on" : "cell-off"}`}
      onClick={() => handleCellClick(setCellVal, cellVal)}
    >
      {cellVal}
    </button>
  );
};

export default hot(module)(Cell);
