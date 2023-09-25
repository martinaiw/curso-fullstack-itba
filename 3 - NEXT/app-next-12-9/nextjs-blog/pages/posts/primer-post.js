import Head from "next/head";
import Link from "next/link";
import Script from "next/script";
import Layout from "../../components/Layout";

function PrimerPost() {
    return (
        <Layout>
            <Head>
                <title>Primer Post</title>
            </Head>

            <h1>Primer post</h1>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus tempor rhoncus est, nec fermentum enim sollicitudin vel. Phasellus iaculis nulla facilisis arcu accumsan, a volutpat risus accumsan. Duis luctus vitae justo ut facilisis. Vivamus in ultrices lacus. Donec sollicitudin ornare ultricies. Suspendisse a volutpat nisi. Suspendisse potenti. Aliquam erat volutpat. Cras sem orci, consectetur sodales imperdiet sit amet, cursus tincidunt ligula. Quisque fringilla ornare luctus. </p>
            <h2>
                <Link href="/">Volver al inicio</Link>
            </h2>
        </Layout>
    );
}

export default PrimerPost;



{/* <Script
    src="https://connect.facebook.net/en_US/sdk.js"
    strategy="lazyOnload"
    onLoad={() => console.log(`Script cargado correctamente`)}/> */}