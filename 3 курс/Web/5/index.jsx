class Hello extends React.Component {
    render() {
        return <h1>Hello, React</h1>;
    }
}

class TODO extends React.Component {
    
  constructor(props) {
    super(props);
    this.state = { items: [], text: '' };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.itemRemove = this.itemRemove.bind(this);
  }

  render() {
    return (
      <div class="form-inner">
        <form onSubmit={this.handleSubmit} class="decor">
          <h3>TODO</h3>
          <input
            id="new-todo"
            onChange={this.handleChange}
            value={this.state.text}
            placeholder="New ToDo"
          />
          <button>Add</button>
          <div class="todo-inner">
            <TodoList items={this.state.items} func={this.itemRemove}/>
          </div>
          <div class="form-left-decoration"></div>
          <div class="form-right-decoration"></div>
          <div class="circle"></div>
          <div class="form-inner"></div>
        </form>
      </div>
    );
  }

  handleChange(e) {
    this.setState({ text: e.target.value });
  }

  handleSubmit(e) {
    e.preventDefault();
    if (this.state.text.length === 0) {
      return;
    }
    const newItem = {
      text: this.state.text,
      id: Date.now()
    };
    this.setState(state => ({
      items: state.items.concat(newItem),
      text: ''
    })
    );
  }

  itemRemove(e) {
    for (const i of Array(this.state.items.length).keys()) {
      if (this.state.items[i].id === e) {
        const newState = this.state.items.splice(i, 1)
        this.setState({state: newState});
        break
      }
    }

  }
}

class TodoList extends React.Component {

  render() {
    return (
      <ol>
        {this.props.items.map(item => (
            <li>
              <p id={item.id}>{item.text}  <button onClick={() => this.props.func(item.id)}>✕</button></p>
            </li>
        ))}
      </ol>
    );
  }
}

ReactDOM.render(
    <TODO></TODO>,
    document.getElementById("app")
)
