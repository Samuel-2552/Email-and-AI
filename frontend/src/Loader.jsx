import React from 'react';
import "../src/styles/mystyle.css";
function Loader(props) {
    return (
        <div class="container">
            <div style="--x: 50%; --y: 51%; z-index: 10;--delay:0.1s;"></div>
            <div style="--x: 50%; --y: 51.5%; z-index: 9; --delay:0.3s;"></div>
            <div style="--x: 50%; --y: 52%; z-index: 8; --delay:0.5s;"></div>
            <div style="--x: 50%; --y: 52.5%; z-index: 7; --delay:0.7s;"></div>
        </div>
    );
}

export default Loader;