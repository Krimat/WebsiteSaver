import SiteCard from '../SiteCard'
import {Row, Col} from 'reactstrap'


export default function Grid(props) {
    return (
        <>
            
            <Row xs={props.colNumber}>
                {props.sites.map(site=>{return (
                <>  
                    <Col key={site.id}>
                        <SiteCard
                        key={site.id}
                        site={site}
                        defaultImage={props.defaultImage}
                        />
                    </Col>
                </>
                )})}
            </Row>
            
        </>
    );
}