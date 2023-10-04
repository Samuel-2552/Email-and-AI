import React, { useEffect } from 'react';
import $ from 'jquery'
import NylasLogo from "../src/utils/logo1.png"
import Background from "../src/utils/background1.jpg"
import "../src/styles/mystyle.css"

function NylasLanding({setGetStart}) {
    useEffect(() => {
        $(".base").clone().addClass("overlay").appendTo(".landing");
        $(".cta").on('mouseover', function () {
            $(".overlay").toggleClass("over");
        });
        setTimeout(function () {
            $(".overlay")
                .addClass("over")
                .delay(600)
                .queue(function () {
                    $(this).removeClass("over").dequeue();
                });
        }, 400);
    },[])
    return (
        <div class="landing">
            <div class="base">
                <div class="image">
                    <img src={Background} alt="background" />
                </div>
                <div class="copy">
                    <div class="logo">
                        <img src={NylasLogo} width="100px" height="auto" alt="Logo" />
                    </div>
                    <div class="title">
                        <small>Unlock the Power of Your Inbox with Attachment Summarization</small> Nylas and AI!
                    </div>
                    <div class="text">
                        Discover the revolutionary tool <br />
                        that transforms your email experience. <br />
                        Our Attachment Summarization feature <br />
                        intelligently analyzes all the attachments <br />
                        you've received in your mailbox, <br />
                        saving you valuable time and effort.

                    </div>
                    {/* <a class="cta">Try Now!</a> */}
                    <button className='cta' onClick={() => setGetStart(true)}>Try Now!</button>
                </div>
            </div>
        </div>
    )

    {/* <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script> */ }


    {/* <script>
                                $(".base").clone().addClass("overlay").appendTo(".landing");
                                $(".cta").hover(function () {
                                    $(".overlay").toggleClass("over");
                            });
                                setTimeout(function () {
                                    $(".overlay")
                                        .addClass("over")
                                        .delay(600)
                                        .queue(function () {
                                            $(this).removeClass("over").dequeue();
                                        });
        }, 400);

                            </script> */}


}

export default NylasLanding;