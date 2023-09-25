import {useRouter} from 'next/router';
import Layout from '../../components/Layout';

export default function Page(){
    const router = useRouter();
    return (
        <Layout>
            El post ingresado es: {router.query.id}
        </Layout>
    );
}