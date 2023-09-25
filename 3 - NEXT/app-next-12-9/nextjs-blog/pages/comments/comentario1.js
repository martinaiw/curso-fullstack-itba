import Head from 'next/head';
import Link from 'next/link';
import Layout from '../../components/Layout.js';

function Comentario1() {

    return (

        <Layout>
            <Head>
                <nav></nav>
                <title>Comentarios</title>
            </Head>
            <h1>Comentario:</h1>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                Phasellus tempor rhoncus est, nec fermentum enim sollicitudin vel.</p>
            <h2>
                <Link href="/">Volver al inicio</Link>
            </h2>
        </Layout>
    );

}
export default Comentario1