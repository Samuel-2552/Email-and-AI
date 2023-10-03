import React from 'react';
import PropTypes from 'prop-types';
import '../src/styles/mystyle.css'
import { useState } from 'react';
import $ from 'jquery'

function EmailAttachments({
    emails,
    setToastNotification,
    serverBaseUrl,
    userId
}) {
    const [filename, setFileName] = useState('')
    const [data, setData] = useState([]);
    const [error, setError] = useState(null);
    const [isImage, setIsImage] = useState(false);
    async function getInsights(email) {
        // const url = { serverBaseUrl } + "/process_file?id=" + email[1] + "&email=" + email[0]
        setData()
        setError(null)
        setFileName(email[0])
        setIsImage(false)
        const date = new Date();
        const url = "http://127.0.0.1:9000/process_file?id=" + email[1] + "&filename=" + email[0]
        console.log(url);
        await fetch(url, {
            method: 'GET',
            headers: {
                Authorization: userId,
                'Content-Type': 'application/json',
            }})
            .then((response) => {
                console.log(response)
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then((responseData) => {
                console.log(responseData);
                if(responseData['isImage']) {
                    setIsImage(true)
                }
                setData(responseData[email[0]]);
            })
            .catch((error) => {
                console.log(error)
                setError(error);
            });
    }
    return (
        <>
            <div className='att-container'>
                {
                    emails.map(function (email, index) {
                        return (
                            <div key={index} className='att-items' onClick={() => getInsights(email)}>
                                <b>{email[0]}</b>
                            </div>
                        );
                    })
                }
            </div>
            <div className='att-item-viewer'>
                {filename !== ''?<h3>Summary of the {filename}</h3>:<span></span>}
                {
                    isImage?<img src={data} className='graph_image'/>:<h4>{data}</h4>
                }

            </div>
        </>
    );
}


EmailAttachments.propTypes = {
    emails: PropTypes.array.isRequired,
    setToastNotification: PropTypes.func.isRequired,
};

export default EmailAttachments;
