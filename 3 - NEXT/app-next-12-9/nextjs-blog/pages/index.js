import Head from 'next/head';
import styles from '../styles/Home.module.css';
import Link from 'next/link';
import Layout from '../components/Layout';

export default function Home() {
  return (
    <Layout>
      <Head>
        <title>Blogs - ITBA</title>
      </Head>

      <h1 className={styles.title}>Blogs</h1>
      <h2>
        Ir a <Link href="posts/primer-post">Blogs</Link>
      </h2>
      <h2>
        Ir a <Link href="comments/comentario1">Comentarios</Link>
      </h2>
    </Layout>
  );
}
