import React from "react";
import { hot } from "react-hot-loader";

import "./Cell.css";

const Cell = (props) => {
  const { value, handleCellClick } = props;

  return <button onClick={handleCellClick}>{value}</button>;
};

export default hot(module)(Cell);
