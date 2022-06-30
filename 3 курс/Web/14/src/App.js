import React from "react";

class App extends React.Component {
  constructor() {
    super();
    this.array = ["Привет, мам! Жду тебя дома", "Перезвони мне"];
    this.state = {
      isLoggedIn: false
    };
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {
    this.setState((st) => {
      return {
        isLoggedIn: !st.isLoggedIn
      };
    });
  }

  render() {
    const listItems = this.array.map((number) => <li>{number}</li>);

    if (this.state.isLoggedIn) {
      return (
        <div>
          <button onClick={this.handleClick}>LOG OUT</button>
          <p>Входящие:{this.messages}</p>
          <ul>{listItems}</ul>
        </div>
      );
    }

    return (
      <div>
        <button onClick={this.handleClick}>LOG IN</button>
      </div>
    );
  }
}

export default App;
