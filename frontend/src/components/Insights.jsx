import React, { useState } from 'react';
import "../styles/mystyle.css";

function Insights() {
    const [fullScreen, setFullScreen] = useState('')

    return (
        <div className="graph-images">
            <div>
                <img src="http://127.0.0.1:9000/static/graph1.png" className='images' />
            </div>
            <div>
                <img src="http://127.0.0.1:9000/static/graph2.png" className='images' />
            </div>
            <div>
                <img src="http://127.0.0.1:9000/static/graph3.png" className='images' />
            </div>
            <div>
                <img src="http://127.0.0.1:9000/static/graph4.png" className='images' />
            </div>
            <div>
                <img src="http://127.0.0.1:9000/static/graph5.png" className='images' />
            </div>
            <div>
                <img src="http://127.0.0.1:9000/static/graph6.png" className='images' />
            </div>

            {fullScreen && (
                <div
                    id="fullScreenImage"
                    onClick={() => setFullScreen('')}
                    className="full-screen-container"
                >
                    <img
                        src={fullScreen}
                        alt="Full-screen image"
                        className="full-screen-image"
                    />
                </div>
            )}
        </div>
    );
}

export default Insights;