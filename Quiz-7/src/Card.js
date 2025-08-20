import React from "react";

// Reusable Card component
function Card({ title, content }) {
  const styles = {
    border: "1px solid #ddd",
    borderRadius: "12px",
    padding: "20px",
    margin: "10px 0",
    boxShadow: "2px 2px 10px rgba(0,0,0,0.1)"
  };

  return (
    <div style={styles}>
      <h3>{title}</h3>
      <p>{content}</p>
    </div>
  );
}

export default Card;
