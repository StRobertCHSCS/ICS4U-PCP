using UnityEngine;
using System.Collections;

public class BulletHole : MonoBehaviour {
    public static int numOfHoles = 0;
    private float counter = 0;
    private float timeToDestroy = 5;

	// Use this for initialization
	void Start ()
    {
	
	}
	
	// Update is called once per frame
	void Update ()
    {
        counter += Time.deltaTime;
        if (counter >= timeToDestroy)
        {
            Destroy(this.gameObject);
        }
        if (WoodDestruction.woodDestroy == true) 
        {
            Destroy(this.gameObject);
        }
    }
}
