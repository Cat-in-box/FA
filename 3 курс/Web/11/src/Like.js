import "./styles.css";

export default function Like() {
  return (
    <div className="Like" align="right">
      <button onClick={(e) => (e.target.style.color = "red")}>♥</button>
    </div>
  );
}
