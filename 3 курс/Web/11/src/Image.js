import "./styles.css";

export default function Image() {
  return (
    <div className="Image">
      <img src={require("./img.png")} alt="это кот"></img>
    </div>
  );
}
