import React from 'react';
import PropTypes from 'prop-types';
import '../src/styles/mystyle.css'
import { useState } from 'react';
import $ from 'jquery'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faFilePdf, faFileImage, faFileExcel, faFileWord, faFilePowerpoint, faFile } from '@fortawesome/free-solid-svg-icons';
import './styles/email.scss';


function EmailAttachments({
    emails,
    setToastNotification,
    serverBaseUrl,
    userId
}) {
    const [filename, setFileName] = useState('')
    const [data, setData] = useState('');
    const [error, setError] = useState(null);
    const [isImage, setIsImage] = useState(false);

    const icon = {
        'faFilePdf': <FontAwesomeIcon icon={faFilePdf}/>,
        'faFileImage': <FontAwesomeIcon icon={faFileImage}/>,
        'faFileExcel': <FontAwesomeIcon icon={faFileExcel}/>,
        'faFileWord': <FontAwesomeIcon icon={faFileWord}/>,
        'faFilePowerpoint': <FontAwesomeIcon icon={faFilePowerpoint}/>
    }
    async function getInsights(email) {
        // const url = { serverBaseUrl } + "/process_file?id=" + email[1] + "&email=" + email[0]
        setData('')
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
                        email[0] = email[0].replace("_", " ");
                        var logo = "";
                        if(email[0].length >= 50){
                            const ext = email[0].split('.').pop();
                            const file = email[0].slice(0,-ext.length - 1);
                            const trun_file = file.slice(0, 50 - ext.length - 1)
                            email[0] = `${trun_file}...${ext}`
                        }
                        return (
                            <div key={index} className='att-items' onClick={() => getInsights(email)}>
                                <b>{email[0]}</b>
                                <div className='file-logo'>
                                    {
                                        icon[email[2]]
                                    }
                                </div>
                            </div>
                        );
                    })
                }
            </div>
            <div className='att-item-viewer'>
                {filename !== ''?<h3>Summary of the {filename}</h3>:<span></span>}
                {
                    isImage?<img src={data} className='graph_image'/>:data === '' && filename !== ''?<p className="loading" style={{color: 'white'}}>Loading emails...</p>:<h4><br/>{data}</h4>

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
