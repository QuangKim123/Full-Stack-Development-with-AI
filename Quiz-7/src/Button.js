import React from "react";

// Reusable Button component
function Button({ label, onClick, color = "blue" }) {
  const styles = {
    padding: "10px 20px",
    margin: "5px",
    border: "none",
    borderRadius: "8px",
    backgroundColor: color,
    color: "white",
    cursor: "pointer"
  };

  return (
    <button style={styles} onClick={onClick}>
      {label}
    </button>
  );
}

export default Button;
