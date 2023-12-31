import React, { useState, useEffect } from 'react';
import { useNylas } from '@nylas/nylas-react';
import NylasLogin from './NylasLogin';
import Layout from './components/Layout';
import EmailApp from './EmailApp';
import NylasLanding from './NylasLanding';

function App() {
  const nylas = useNylas();
  const [userId, setUserId] = useState('');
  const [userEmail, setUserEmail] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [emails, setEmails] = useState([]);
  const [toastNotification, setToastNotification] = useState('');
  const SERVER_URI = import.meta.env.VITE_SERVER_URI || 'http://127.0.0.1:9000';
  const [getStart, setGetStart] = useState(false);
  const [insights, setInsights] = useState(false);
  const [insightsclick, setInsightsclick] = useState(false);
  useEffect(() => {
    if (!nylas) {
      return;
    }

    // Handle the code that is passed in the query params from Nylas after a successful login
    const params = new URLSearchParams(window.location.search);
    if (params.has('code')) {
      nylas
        .exchangeCodeFromUrlForToken()
        .then((user) => {
          const { id } = JSON.parse(user);
          setUserId(id);
          setGetStart(true);
          sessionStorage.setItem('userId', id);
        })
        .catch((error) => {
          console.error('An error occurred parsing the response:', error);
        });
    }
  }, [nylas]);

  useEffect(() => {
    const userIdString = sessionStorage.getItem('userId');
    const userEmail = sessionStorage.getItem('userEmail');
    if (userIdString) {
      setUserId(userIdString);
      setGetStart(true);
    }
    if (userEmail) {
      setUserEmail(userEmail);
    }
  }, []);

  useEffect(() => {
    if (userId?.length) {
      window.history.replaceState({}, '', `/?userId=${userId}`);
      getEmails();
    } else {
      window.history.replaceState({}, '', '/');
    }
  }, [userId]);

  const getEmails = async () => {
    setIsLoading(true);
    try {
      // const url = SERVER_URI + '/nylas/read-emails';
      const url = SERVER_URI + '/download';
      const res = await fetch(url, {
        method: 'GET',
        headers: {
          Authorization: userId,
          'Content-Type': 'application/json',
        },
      });
      const data = await res.json();

      if (Array.isArray(data)) {
        setEmails(data);
      } else {
        setEmails([]);
      }
      // console.log(emails)
    } catch (e) {
      console.warn(`Error retrieving emails:`, e);
      return false;
    }
    setIsLoading(false);
  };

  const disconnectUser = () => {
    sessionStorage.removeItem('userId');
    sessionStorage.removeItem('userEmail');
    setUserId('');
    setUserEmail('');
  };

  const refresh = () => {
    getEmails();
  };

  return (

    <>
    {
      !getStart ? (<NylasLanding setGetStart={setGetStart}/>) : 
      <Layout
      showMenu={!!userId}
      disconnectUser={disconnectUser}
      refresh={refresh}
      isLoading={isLoading}
      title="Email Attachments Summary and Insights"
      toastNotification={toastNotification}
      setToastNotification={setToastNotification}
      setInsights = {setInsights}
      setInsightsclick = {setInsightsclick}
      userId={userId}
    >
      {
          !userId ? (
            <NylasLogin email={userEmail} setEmail={setUserEmail} />
          ) : (
            <div className="app-card">
              <EmailApp
                userEmail={userEmail}
                emails={emails}
                isLoading={isLoading}
                serverBaseUrl={SERVER_URI}
                userId={userId}
                reloadEmail={refresh}
                setToastNotification={setToastNotification}
                insights={insights}
                insightsclick={insightsclick}
              />
            </div>
          )}
    </Layout>
    }
    </>
  );
}

export default App;
