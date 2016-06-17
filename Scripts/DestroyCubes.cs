using UnityEngine;
using System.Collections;

public class DestroyCubes : MonoBehaviour
{
	public GameObject enemySphere;
	void Start(){

	}

	void OnCollisionEnter (Collision col)
	{
		if (col.gameObject.tag == "Enemy") {
			EnemyHealthScript ehs = col.gameObject.GetComponent<EnemyHealthScript> ();
			ehs.health -= 1;
			GameObject bhole = Instantiate (enemySphere, this.gameObject.transform.position, this.gameObject.transform.rotation) as GameObject;
			bhole.transform.parent = col.gameObject.transform;

			Destroy (this.gameObject);

		} else if (col.gameObject.tag == "Terrain" || col.gameObject.tag == "Untagged") {

			Destroy (this.gameObject);

		} 
		else if (col.gameObject.tag == "Wall") {

			Destroy (this.gameObject);

		}


	}
}