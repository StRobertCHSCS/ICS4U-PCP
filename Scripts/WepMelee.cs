using UnityEngine;
using System.Collections;

public class WepMelee : MonoBehaviour {
	//public GameObject enemy;
	public GameObject cylinder;

	void Start(){

	}

	// Update is called once per frame
	public void Update () {
		if (Input.GetButton ("Fire1")) {
			Attack ();
			}
		}


	void Attack(){
		GameObject cyl = Instantiate (cylinder, transform.position, transform.rotation) as GameObject;
		cyl.transform.parent = transform;
		cyl.GetComponent<Melee> ().Stab ();

	}
}
