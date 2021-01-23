//by Ankita Gupta
class LinkedList
{
    public:
    Node *head;
    Node *tail;

    LinkedList()
    {
        head=NULL;
        tail=NULL;
    }

    Node * createLL()
    {
        head=NULL, tail=NULL;

        int data;
        cin>>data;
        
        while(data!=-1)
        {
            Node *temp= new Node(data);

            if(head==NULL)
            {
                head=temp;
                tail=temp;
            }
            else{
                tail->next=temp;
                tail=tail->next;
            }

            cin>>data;
        }
        return head;
    }  

    void printLL(Node *head)
    {
        while(head!=NULL)
        {
            cout<<head->data<<" ";
            head=head->next;
        }
        return;
    }

    ~LinkedList()
    {
        delete head;
        delete tail;
    }


};
