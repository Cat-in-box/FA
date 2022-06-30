'use strict';

const e = React.createElement;

class LikeButton extends React.Component {
    constructor(props) {
        super(props);
        this.state = { liked: false };
    }

    render() {
        if (this.state.liked) {
            return 'Purrfect choice -> №' + this.props.catID;
        }
        return e(
            'button',
            { onClick: () => this.setState({ liked: true}) },
            'Like'
        );
    }
}

document.querySelectorAll('#like_button_container').forEach(domContainer => {
    const catID = parseInt(domContainer.dataset.catid, 10);
    ReactDOM.render(e(LikeButton, {catID: catID}), domContainer);
});

//const domContainer = document.querySelector('#like_button_container');
//ReactDOM.render(e(LikeButton), domContainer);
