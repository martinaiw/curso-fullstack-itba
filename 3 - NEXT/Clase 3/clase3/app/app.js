import Script from 'next/script';

function App({ Component, pageProps }) {
  return (
    <>
      <Script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.29.1/moment.min.js" />
      <Component {...pageProps} />
    </>
  );
}

export default App;
