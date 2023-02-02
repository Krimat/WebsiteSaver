import {useState} from 'react'
import {Card, CardImg, CardTitle, Modal, ModalBody, ModalHeader, ModalFooter, Button} from 'reactstrap'



export default function SiteCard(props) {
    const [modal, setModal] = useState(false);
    const toggle = () => setModal(!modal);

    const openSite = () => {
        window.open(props.site.url, '_blank', 'noopener,noreferrer')
    }
    return (
        <>
           <Card>
                <CardImg
                src={props.site.image ? props.site.image : props.defaultImage}
                width="50%"
                top
                />
                <CardTitle className='w-100 text-center'>
                    {props.site.name}
                </CardTitle>
                <Button 
                onClick={toggle} 
                color="dark"
                className='m-1'
                >
                    View
                </Button>
                <Modal 
                isOpen={modal}
                backdrop={true}
                >
                    <ModalHeader toggle={toggle}>{props.site.name}</ModalHeader>
                    <ModalBody>
                        {props.site.description}
                    </ModalBody>
                    <ModalFooter>
                        <Button>
                            Open Site
                        </Button>
                    </ModalFooter>
                </Modal>
                
            </Card> 
        </>
    );
};