class ClickButton extends React.Component {

  constructor(props) {
      super(props);
      this.state = {class: "off", label: "Нажми"};
         
      this.press = this.press.bind(this);
         
      console.log("constructor");
  }
  static getDerivedStateFromProps(props, state) {
       console.log("getDerivedStateFromProps()");
       return null;
  }
  componentDidMount(){
      console.log("componentDidMount()");
  }
  componentWillUnmount(){
      console.log("componentWillUnmount()");
  }
  shouldComponentUpdate(){
      console.log("shouldComponentUpdate()");
      return true;
  }
  getSnapshotBeforeUpdate(prevProps, prevState) {
     console.log("getSnapshotBeforeUpdate()");
     return null;
 }
  componentDidUpdate(){
      console.log("componentDidUpdate()");
  }
  press(){
      var className = (this.state.class==="off")?"on":"off";
      this.setState({class: className});
  }
  render() {
      console.log("render()");
      return <button onClick={this.press} className={this.state.class}>{this.state.label}</button>;
  }
}



class Clock extends React.Component {
  constructor(props) {
    super(props);
    this.state = {date: new Date()};
    this.unmount = this.unmount.bind(this);
  }
  static getDerivedStateFromProps(props, state) {
       console.log("getDerivedStateFromProps()");
       return null;
  }
  componentDidMount() {
    this.timerId = setInterval(
      ()=> this.tick(),
      1000
    );
    console.log("componentDidMount()");
  }
  componentWillUnmount() {
    clearInterval(this.timerId);
    console.log("componentWillUnmount()");
  }
  shouldComponentUpdate(){
      console.log("shouldComponentUpdate()");
      return true;
  }
  getSnapshotBeforeUpdate(prevProps, prevState) {
     console.log("getSnapshotBeforeUpdate()");
     return null;
 }
  componentDidUpdate(){
      console.log("componentDidUpdate()");
  }

  press(){
      var className = (this.state.class==="off")?"on":"off";
      this.setState({class: className});
  }

  unmount(){
      ReactDOM.unmountComponentAtNode(document.getElementById("clock"));
  }

  tick() {
    this.setState({
      date: new Date()
    });
  }

  render() {
    return (
      <div>
        <h3>Текущее время: {this.state.date.toLocaleTimeString()}.</h3>
        <button onClick={this.unmount}>Использовать unmount</button>
      </div>
    );
  }
}

ReactDOM.render(
    <Clock />,
    document.getElementById("clock")
)



const propsValues = {
    title: "Список группы",
    items: [
        "Студент 1", 
        "Студент 2", 
        "Студент 3", 
        "Студент 4", 
        "Студент 5", 
        "Студент 6"
    ]
};
              
class Item extends React.Component {
    render() {
        return <p class="item">{this.props.name}</p>;
    }
}
         
class SearchPlugin extends React.Component{
             
    constructor(props){
        super(props);
        this.onTextChanged = this.onTextChanged.bind(this);
    }
             
    onTextChanged(e){
        var text = e.target.value.trim();   // удаляем пробелы
        this.props.filter(text); // передаем введенный текст в родительский компонент
    }
             
    render() {
        return <input placeholder="Поиск" onChange={this.onTextChanged} />;
    }
}
                  
class ItemsList extends React.Component {
    constructor(props){
        super(props);
        this.state = { items: this.props.data.items};
                          
        this.filterList = this.filterList.bind(this);
    }
             
    filterList(text){
        var filteredList = this.props.data.items.filter(function(item){
            return item.toLowerCase().search(text.toLowerCase())!== -1;
        }); 
        this.setState({items: filteredList});
    }
              
    render() {
        return(
            <div class="studentsList">
              <div class="form-inner">
                <h2>{this.props.data.title}</h2>
                <SearchPlugin filter={this.filterList} />
              </div>
              <ul class="form-content">
                  {
                      this.state.items.map(function(item){
                          return <Item key={item} name={item} />
                      })
                  }
              </ul>
            </div>);
    }
}
          
ReactDOM.render(
    <ItemsList data={propsValues} />,
    document.getElementById("app")
)