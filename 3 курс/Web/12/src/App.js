import "./styles.css";
import React from "react";

class ProductFilter extends React.Component {
  constructor(props) {
    super(props);
    this.handleFormInput = this.handleFormInput.bind(this);
    this.state = {
      series: 0,
      price: 0
    };
  }

  handleFormInput(series, price) {
    this.setState({
      series: series,
      price: price
    });
  }

  render() {
    const products = [
      {
        name:
          "Шоколадное яйцо Kinder Сюрприз Applaydu, классическая коллекция, коробка 36 шт.",
        price: 3279,
        series: "Продукты",
        uri:
          "https://avatars.mds.yandex.net/get-mpic/4055794/img_id4524449845225591889.jpeg/orig"
      },
      {
        name:
          "Сухой корм для стерилизованных кошек Royal Canin Sterilised 37 2 кг",
        price: 1498,
        series: "Для животных",
        uri:
          "https://avatars.mds.yandex.net/get-mpic/5191276/img_id4772248367753456537.png/orig"
      },
      {
        name: "Смартфон Samsung Galaxy A51 4/64 ГБ, белый",
        price: 23000,
        series: "Электроника",
        uri:
          "https://avatars.mds.yandex.net/get-mpic/5191310/img_id4410669965894415578.png/orig"
      },
      {
        name: "Молоко Простоквашино пастеризованное 2.5%, 0.93 л",
        price: 178,
        series: "Продукты",
        uri:
          "https://avatars.mds.yandex.net/get-mpic/4944925/img_id4999161222536329731.jpeg/orig"
      },
      {
        name: "Съедобная игрушка",
        price: 124,
        series: "Для животных",
        uri:
          "https://avatars.mds.yandex.net/get-mpic/4732637/img_id2168022172044250128.jpeg/orig"
      },
      {
        name: "Беспроводные наушники Cat ear P33M (bluetooth+microSD+FM)",
        price: 1350,
        series: "Электроника",
        uri:
          "https://avatars.mds.yandex.net/get-mpic/5324096/img_id5005297802040278362.jpeg/orig"
      },
      {
        name:
          "Шебекинские Макароны Спирали Три цвета № 366.5 с томатами и шпинатом, 450 г",
        price: 71,
        series: "Продукты",
        uri:
          "https://avatars.mds.yandex.net/get-mpic/5042167/img_id6054128111345702510.jpeg/orig"
      },
      {
        name: "Пуфик для животных c узором (радужный, D 50 см)",
        price: 999,
        series: "Для животных",
        uri:
          "https://avatars.mds.yandex.net/get-mpic/5235128/img_id3708870225493620745.jpeg/orig"
      },
      {
        name: "Игровая приставка Sony PlayStation 5 825 ГБ SSD, белый",
        price: 82990,
        series: "Электроника",
        uri:
          "https://avatars.mds.yandex.net/get-mpic/4080439/img_id3396893556724706605.jpeg/orig"
      },
      {
        name: "Соус Heinz Кисло-сладкий, 230 г",
        price: 96,
        series: "Продукты",
        uri:
          "https://avatars.mds.yandex.net/get-mpic/4304063/img_id416600128077150444.jpeg/orig"
      }
    ];

    return (
      <div className="filter">
        <div className="header">
          <a>А.Маркет</a>
          <MainFilterMenu
            series={this.state.series}
            price={this.state.price}
            onFormInput={this.handleFormInput}
          />
        </div>
        <ProductFilterResults
          products={products}
          series={this.state.series}
          price={this.state.price}
        />
      </div>
    );
  }
}

class MainFilterMenu extends React.Component {
  constructor(props) {
    super(props);
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange() {
    this.props.onFormInput(
      this.refs["seriesInput"].value,
      this.refs["priceInput"].checked
    );
  }

  render() {
    return (
      <form className="filter-menu">
        <label form="priceInput">По цене</label>
        <input
          id="priceInput"
          type="checkbox"
          checked={this.props.price}
          ref="priceInput"
          onChange={this.handleChange}
        />
        <br />
        <label form="seriesInput">По категории:</label>
        <br />
        <select id="seriesInput" ref="seriesInput" onChange={this.handleChange}>
          <option value="Все">Всё</option>
          <option value="Электроника">Электроника</option>
          <option value="Для животных">Для животных</option>
          <option value="Продукты">Продукты</option>
        </select>
      </form>
    );
  }
}

class ProductFilterResults extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    const results = [];

    if (this.props.price === true) {
      this.props.products.sort((a, b) => {
        return b.price - a.price;
      });
    }

    this.props.products.map((product) => {
      if (this.props.series === 0 || this.props.series === "Все") {
        results.push(<Product product={product} />);
      } else if (product.series === this.props.series) {
        results.push(<Product product={product} />);
      }
    });

    return (
      <div className="filter-results">
        <ul className="blocks blocks_3up">{results}</ul>
      </div>
    );
  }
}

class Product extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <li>
        <div className="feature">
          <div className="feature-hd">
            <h2 class="hdg hdg_2">{this.props.product.name}</h2>
          </div>
          <div className="feature-bd">
            <p>{this.props.product.series}</p>
          </div>
          <div className="feature-image">
            <img src={this.props.product.uri} alt="new" />
          </div>
          <div className="feature-ft">
            <p>
              <b>{this.props.product.price} ₽</b>
            </p>
          </div>
        </div>
      </li>
    );
  }
}

export default ProductFilter;
