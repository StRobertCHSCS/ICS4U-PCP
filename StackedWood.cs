using UnityEngine;
using System.Collections;

public class StackedWood : MonoBehaviour {
    public static bool stackedHit = false;
    public GameObject debrisPrefab;
    public Rigidbody rb;
    private float timer = 0;
    private float counter = 0.53f;

    // Use this for initialization
    void Start () {
        rb = gameObject.GetComponent<Rigidbody>();
    }
	
	// Update is called once per frame
	void Update ()
    {
        RaycastHit hit;
        Ray ray = new Ray(transform.position, -transform.up);
        if (Physics.Raycast(ray, out hit, 5f))
        {
            Debug.DrawLine(transform.position, hit.point, Color.green);
            if (hit.collider.tag != "Wood" && hit.collider.tag != "Player")
            {
                rb.AddForce(Physics.gravity * rb.mass * 2.75f);
                rb.isKinematic = false;
                timer += Time.deltaTime;

                if (timer > counter) {
                    Destroy(this.gameObject);
                    Instantiate(debrisPrefab, transform.position, transform.rotation);
                }
            }
        }
	}
}
