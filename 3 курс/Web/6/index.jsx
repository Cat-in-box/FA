class Hello extends React.Component {
             
  constructor(props) {
      super(props);
      this.activeName = this.props.name;
      this.activeAge = this.props.age;
      this.state = {class: "off", label: "Hide"};
      this.press = this.press.bind(this);
  }
  press(){
      let className = (this.state.class==="off")?"on":"off";
      this.activeName = (this.state.class==="on")?this.props.name:"????";
      this.activeAge = (this.state.class==="on")?this.props.age:"????";
      this.setState({class: className});
  }
  render() {
      return <div class="postcard">
          <div class="form-row">
            <label>Имя:</label><p type="text" id="name" required>{this.activeName}</p>
          </div>
          <div class="form-row">
            <label>Возраст:</label><p type="text" id="name" required>{this.activeAge}</p>
          </div>
          <div class="form-row">
            <button onClick={this.press} className={this.state.class}>{this.state.label}</button>
          </div>
      </div>
      
  }
}

ReactDOM.render(
  <Hello name="Жевагина Анастасия" age="20" />,
  document.getElementById("app")
)