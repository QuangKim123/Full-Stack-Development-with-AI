import React from "react";
import Button from "./Button";
import Card from "./Card";

function App() {
  // Example click handlers
  const handleLogin = () => alert("Login button clicked!");
  const handleSubmit = () => alert("Form submitted!");
  const handleLoadMore = () => alert("Loading more content...");

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h1>Reusable Components Demo</h1>

      <h2>Buttons</h2>
      <Button label="Login" onClick={handleLogin} color="green" />
      <Button label="Submit" onClick={handleSubmit} color="blue" />
      <Button label="Load More" onClick={handleLoadMore} color="purple" />

      <h2>Cards</h2>
      <Card
        title="Product Card"
        content="This is a product card. It can display product details."
      />
      <Card
        title="User Profile"
        content="This is a user profile card showing user details."
      />
      <Card
        title="News Article"
        content="This card displays a short news article preview."
      />
    </div>
  );
}

export default App;
