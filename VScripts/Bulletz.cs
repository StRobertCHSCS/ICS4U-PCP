using UnityEngine;
using System.Collections;

public class Bulletz : MonoBehaviour
{

	public Rigidbody rb;
    public float secondsToDestroy = 5;
    public float speed = 2f;
    public GameObject bullethole;
    private float counter = 0;

    

    // Use this for initialization
    void Start()
    {
		rb = gameObject.GetComponent<Rigidbody> ();
    }

    // Update is called once per frame
    void FixedUpdate()
    {
        counter += Time.deltaTime;
        transform.Translate(0, 0, speed);
        RaycastHit hit;
        Ray ray = new Ray(transform.position, transform.forward);
        if (Physics.Raycast(ray, out hit, 3f))
        {
            if (hit.collider.tag == "Enemy")
            {
				rb.isKinematic = true; 
				// sets trigger in EnemyAI.cs
				if (speed == 2) 
				{
					EnemyAI.initialHit = true;
				} 
            }
			else if (hit.collider.tag == "Wood" || hit.collider.tag == "WoodBelow") 
            {
                if (speed == 2)
                {
                    // sets trigger in WoodDestruction to ensure bullet does not increase destruction stage of two walls at the same time

                    WoodDestruction.initialHit = true;
                    WoodDestruction.hitWoodAbove = false;
                }
                if (speed >= 0)
                {
					GameObject bhole = Instantiate(bullethole, hit.point, Quaternion.FromToRotation(Vector3.up, hit.normal)) as GameObject;
					bhole.transform.parent = hit.collider.gameObject.transform;
                    speed -= 0.25f;
                }
            }
            else if (hit.collider.tag == "WoodAbove")
            {

                if (speed == 2)
                {
                    // sets trigger in WoodDestruction to ensure bullet does not increase destruction stage of two walls at the same time
                    WoodDestruction.initialHit = true;
                    WoodDestruction.hitWoodAbove = true;
                    
                }
                if (speed >= 0)
                {
					GameObject bhole = Instantiate(bullethole, hit.point, Quaternion.FromToRotation(Vector3.up, hit.normal)) as GameObject;
                    speed -= 0.25f;
                }
            }
               
            else if (hit.collider.tag == "Debris")
            {
                if (woodDebris.settled == true)
                {
                    Destroy(this.gameObject);
					GameObject bhole = Instantiate(bullethole, hit.point, Quaternion.FromToRotation(Vector3.up, hit.normal)) as GameObject;
                }
            }
            else
            {
				GameObject bhole = Instantiate(bullethole, hit.point, Quaternion.FromToRotation(Vector3.up, hit.normal)) as GameObject;
                Destroy(this.gameObject);
                // trigger to set woodDestroy false so that bulletholes can be made again
                WoodDestruction.woodDestroy = false;
            }
        }
        // ensures that too many bullets do not clog up memory
        if (counter > secondsToDestroy)
        {   
            Destroy(this.gameObject);
        }
        // ensure no bullet bounceback behaviour 
        if (speed < 0)
        {
            Destroy(this.gameObject);
        }
    }
}
