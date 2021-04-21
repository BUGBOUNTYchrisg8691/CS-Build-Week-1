import React from "react";
import { hot } from "react-hot-loader";

import "./index.css";

const ResetButton = (props) => {
  const { handleReset } = props;

  return (
    <button className="reset-button" type="submit" onClick={handleReset}>
      Reset
    </button>
  );
};

export default hot(module)(ResetButton);
